import test from 'node:test';
import assert from 'node:assert/strict';
import {initial, record} from './ladder.ts';

test('three clean takes increase the next target', () => {
  const state = [true, true, true].reduce(record, initial);
  assert.equal(state.bpm, 84);
  assert.equal(state.streak, 0);
  assert.equal(state.history[0].bpm, 80);
});
test('a miss resets the streak and tempo stays within bounds', () => {
  const state = [true, false].reduce(record, initial);
  assert.equal(state.streak, 0);
  assert.equal(state.bpm, 76);
  const slow = Array(100).fill(false).reduce(record, initial);
  assert.equal(slow.bpm, 40);
  assert.equal(slow.history.length, 12);
  assert.equal(Array(150).fill(true).reduce(record, initial).bpm, 220);
});
