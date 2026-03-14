import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
// * browser router makes navigation work or enables navigation
// * routes holds all the pages
// * route one specific page/url
// * navigate is used to redirect the user to a different page/url
import { useAuthStore } from './store/authStore'

function App() {
  const { isAuthenticated } = useAuthStore()

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<div>Login Page (coming soon)</div>} />
        <Route path="/register" element={<div>Register Page (coming soon)</div>} />
      
        <Route
          path="/dashboard"
          element={isAuthenticated ? <div>Dashboard (coming soon)</div> : <Navigate to="/login" />}
        />
        <Route path="*" element={<Navigate to={isAuthenticated ? "/dashboard" : "/login"} />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App