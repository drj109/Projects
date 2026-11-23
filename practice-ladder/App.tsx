import React, { useState } from 'react';
import { SafeAreaView, ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { initial, record, type Attempt } from './ladder';

export default function App() {
  const [session, setSession] = useState(initial);
  function button(label: string, onPress: () => void) {
    return <TouchableOpacity accessibilityRole="button" onPress={onPress} style={styles.button}>
      <Text style={styles.buttonText}>{label}</Text>
    </TouchableOpacity>;
  }
  function mark(clean: boolean) { setSession(previous => record(previous, clean)); }
  return <SafeAreaView style={styles.page}><ScrollView contentContainerStyle={styles.content}>
    <Text style={styles.heading}>Practice ladder</Text>
    <Text style={styles.body}>Play a riff at the target tempo on your metronome. Three clean takes earn a faster tempo. A missed take slows it down.</Text>
    <View style={styles.card}><Text style={styles.body}>Target tempo</Text>
    <Text style={styles.tempo}>{session.bpm} BPM</Text>
    <Text>{session.streak} / 3 clean takes</Text></View>
    {button('Clean take', () => mark(true))}
    {button('Missed take', () => mark(false))}
    <Text style={styles.sub}>Recent takes</Text>
    {session.history.length === 0 && <Text>No takes recorded yet.</Text>}
    {session.history.map((a: Attempt) => <Text key={a.id} style={styles.row}>#{a.id}   ·   {a.bpm} BPM   ·   {a.clean ? 'Clean' : 'Missed'}</Text>)}
    {button('Start a new session', () => setSession(initial))}
  </ScrollView></SafeAreaView>;
}
const styles = StyleSheet.create({
  page: {flex: 1, backgroundColor: '#f3efe5'}, content: {padding: 24, paddingTop: 50, gap: 12},
  heading: {fontSize: 36, fontWeight: '700', color: '#23392f'}, sub: {fontSize: 20, fontWeight: '600'},
  body: {fontSize: 16, lineHeight: 23}, card: {backgroundColor: 'white', borderRadius: 12, padding: 20},
  tempo: {fontSize: 40, fontWeight: '700'}, row: {fontSize: 16},
  button: {backgroundColor: '#18513e', padding: 14, borderRadius: 8}, buttonText: {color: 'white', fontSize: 17}
});
