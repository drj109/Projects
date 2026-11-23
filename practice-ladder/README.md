# Practice ladder
A React Native practice log for a guitarist. Each tap records the tempo actually played, then calculates the next target. The log keeps the last twelve attempts in memory.

Use Node 22.13+ and npm. From this folder run `npm install`, `npm test`, `npm run typecheck` and `npm start`. Open with an Expo SDK 54 compatible client or Android emulator. To export the Android JavaScript bundle locally, run `npx expo export --platform android`.

Tap **Clean take** three times. The log should contain three takes at 80 BPM and the next target should be 84 BPM. Tap **Missed take** and check that the target returns to 80. Restarting the app clears the session.

**Make it yours.** Use it during one rehearsal. Add a configurable starting tempo and test how the first recorded take changes.
