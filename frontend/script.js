const API_URL = "http://localhost:8000"; 

const form = document.getElementById('shorten-form');
const input = document.getElementById('long-url');
const result = document.getElementById('result');
const shortUrlLink = document.getElementById('short-url');
const visitBtn = document.getElementById('visit-btn');
const copyBtn = document.getElementById('copy-btn');
const copyFeedback = document.getElementById('copy-feedback');
const submitBtn = document.getElementById('submit-btn');

function setLoading(loading) {
  submitBtn.disabled = loading;
  submitBtn.innerHTML = loading
    ? `<svg class="animate-spin h-5 w-5 mx-auto" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"/><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"/></svg>`
    : 'Shorten';
}

function showError(msg) {
  result.classList.remove('hidden');
  result.innerHTML = `
    <div class="bg-red-500/10 dark:bg-red-500/20 border border-red-500/30 rounded-2xl p-6 text-center">
      <span class="material-symbols-outlined text-red-500 text-4xl mb-3 block">error</span>
      <p class="text-red-600 dark:text-red-400 font-medium">${msg}</p>
    </div>`;
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const url = input.value.trim();
  if (!url) return;

  setLoading(true);
  result.classList.add('hidden');

  try {
    const res = await fetch(`${API_URL}/shorten`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url })
    });

    const data = await res.json();

    if (!res.ok) throw new Error(data.message || data.error || 'Failed to shorten');

    // Success
    shortUrlLink.href = data.shortened_link;
    shortUrlLink.textContent = data.shortened_link;
    visitBtn.href = data.shortened_link;
    result.classList.remove('hidden');
    input.value = '';

  } catch (err) {
    showError(err.message);
  } finally {
    setLoading(false);
  }
});

// Copy to clipboard
copyBtn?.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(shortUrlLink.textContent);
    copyFeedback.classList.remove('hidden');
    setTimeout(() => copyFeedback.classList.add('hidden'), 2000);
  } catch {
    showError('Copy failed');
  }
});

// Theme toggle
const html = document.documentElement;
if (localStorage.theme === 'dark' || (!localStorage.theme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  html.classList.add('dark');
}
document.getElementById('theme-toggle').addEventListener('click', () => {
  html.classList.toggle('dark');
  localStorage.theme = html.classList.contains('dark') ? 'dark' : 'light';
});
