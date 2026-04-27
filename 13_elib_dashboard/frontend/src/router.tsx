import { createBrowserRouter } from "react-router";
import LoginPage from "./pages/Login";
import HomePage from "./pages/Homepage";

const router = createBrowserRouter([
    {   
        path: '/',
        element: <HomePage />
    },
    {
        path: '/login',
        element: <LoginPage />
    }
])

export default router