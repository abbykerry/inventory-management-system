import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { loginUser } from '../services/authService';
import useAuthStore from '../store/authStore';

function LoginPage() {
  const navigate = useNavigate();
  const setAuth = useAuthStore((state) => state.setAuth);

  const [form, setForm] = useState({ email: '', password: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      const data = await loginUser(form);
      setAuth(data.token, data.user);
      navigate('/dashboard');
    } catch (err) {
      const message = err.response?.data?.message || 'Login failed. Please try again.';
      setError(message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.page}>
      <div style={styles.card}>
        <h1 style={styles.title}>Inventory System</h1>
        <h2 style={styles.subtitle}>Sign In</h2>

        {error && <p style={styles.error}>{error}</p>}

        <form onSubmit={handleSubmit} style={styles.form}>
          <label style={styles.label}>Email</label>
          <input
            style={styles.input}
            type="email"
            name="email"
            value={form.email}
            onChange={handleChange}
            placeholder="you@example.com"
            required
            autoComplete="email"
          />

          <label style={styles.label}>Password</label>
          <input
            style={styles.input}
            type="password"
            name="password"
            value={form.password}
            onChange={handleChange}
            placeholder="••••••••"
            required
            autoComplete="current-password"
          />

          <button style={loading ? styles.buttonDisabled : styles.button} type="submit" disabled={loading}>
            {loading ? 'Signing in…' : 'Sign In'}
          </button>
        </form>

        <p style={styles.footer}>
          No account?{' '}
          <Link to="/register" style={styles.link}>
            Register
          </Link>
        </p>
      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: '100vh',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#f3f4f6',
  },
  card: {
    backgroundColor: '#ffffff',
    padding: '2.5rem',
    borderRadius: '8px',
    boxShadow: '0 2px 12px rgba(0,0,0,0.1)',
    width: '100%',
    maxWidth: '400px',
  },
  title: {
    margin: '0 0 0.25rem',
    fontSize: '1.25rem',
    fontWeight: '700',
    color: '#111827',
    textAlign: 'center',
  },
  subtitle: {
    margin: '0 0 1.5rem',
    fontSize: '1rem',
    fontWeight: '400',
    color: '#6b7280',
    textAlign: 'center',
  },
  error: {
    backgroundColor: '#fee2e2',
    color: '#b91c1c',
    padding: '0.75rem',
    borderRadius: '6px',
    fontSize: '0.875rem',
    marginBottom: '1rem',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    gap: '0.5rem',
  },
  label: {
    fontSize: '0.875rem',
    fontWeight: '600',
    color: '#374151',
    marginTop: '0.5rem',
  },
  input: {
    padding: '0.625rem 0.75rem',
    borderRadius: '6px',
    border: '1px solid #d1d5db',
    fontSize: '0.9375rem',
    outline: 'none',
  },
  button: {
    marginTop: '1.25rem',
    padding: '0.75rem',
    backgroundColor: '#2563eb',
    color: '#ffffff',
    border: 'none',
    borderRadius: '6px',
    fontSize: '0.9375rem',
    fontWeight: '600',
    cursor: 'pointer',
  },
  buttonDisabled: {
    marginTop: '1.25rem',
    padding: '0.75rem',
    backgroundColor: '#93c5fd',
    color: '#ffffff',
    border: 'none',
    borderRadius: '6px',
    fontSize: '0.9375rem',
    fontWeight: '600',
    cursor: 'not-allowed',
  },
  footer: {
    marginTop: '1.25rem',
    textAlign: 'center',
    fontSize: '0.875rem',
    color: '#6b7280',
  },
  link: {
    color: '#2563eb',
    textDecoration: 'none',
    fontWeight: '600',
  },
};

export default LoginPage;
