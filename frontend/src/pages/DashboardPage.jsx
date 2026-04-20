import { useNavigate } from 'react-router-dom';
import useAuthStore from '../store/authStore';
import styles from './DashboardPage.module.css';

function DashboardPage() {
  const navigate = useNavigate();
  const user = useAuthStore((state) => state.user);
  const logout = useAuthStore((state) => state.logout);

  const handleLogout = () => {
    logout();
    navigate('/login', { replace: true });
  };

  return (
    <div className={styles.page}>
      <div className={styles.card}>
        <div className={styles.header}>
          <h1 className={styles.title}>Inventory System</h1>
          <button className={styles.logoutButton} onClick={handleLogout}>
            Sign Out
          </button>
        </div>

        <hr className={styles.divider} />

        <h2 className={styles.welcome}>Welcome back{user?.name ? `, ${user.name}` : ''}!</h2>

        {user && (
          <div className={styles.profileCard}>
            <p className={styles.profileRow}>
              <span className={styles.profileLabel}>Name</span>
              <span className={styles.profileValue}>{user.name}</span>
            </p>
            <p className={styles.profileRow}>
              <span className={styles.profileLabel}>Email</span>
              <span className={styles.profileValue}>{user.email}</span>
            </p>
            {user.role && (
              <p className={styles.profileRow}>
                <span className={styles.profileLabel}>Role</span>
                <span className={styles.profileValue}>{user.role}</span>
              </p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default DashboardPage;
