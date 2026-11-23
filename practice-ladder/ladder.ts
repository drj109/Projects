export type Attempt = { id: number; bpm: number; clean: boolean };
type Session = { bpm: number; streak: number; count: number; history: Attempt[] };
export const initial: Session = { bpm: 80, streak: 0, count: 0, history: [] };

export function record(session: Session, clean: boolean): Session {
  const streak = clean ? session.streak + 1 : 0;
  let bpm = session.bpm;
  if (!clean) bpm = Math.max(40, bpm - 4);
  if (streak === 3) bpm = Math.min(220, bpm + 4);
  const id = session.count + 1;
  const take = { id, bpm: session.bpm, clean };
  return { bpm, count: id, streak: streak % 3, history: [take, ...session.history].slice(0, 12) };
}
