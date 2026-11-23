Vue.createApp({
  data() {
    return { skills: 'I scan packages and help with loading', results: [], status: '', busy: false };
  },
  methods: {
    async search() {
      this.busy = true;
      this.results = [];
      this.status = '';
      try {
        const response = await fetch('/api/matches', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ skills: this.skills })
        });
        const body = await response.json();
        if (!response.ok) throw new Error(body.error);
        this.results = body.matches;
        this.status = this.results.length ? 'Closest sample roles' : 'No shared terms. Try a specific task or tool.';
      } catch (error) {
        this.status = error.message;
      } finally {
        this.busy = false;
      }
    }
  }
}).mount('#app');
