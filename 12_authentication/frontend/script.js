const user = document.getElementById('user')
const token = localStorage.getItem('token')
if (!token) {
    document.location.replace('login/login.html')
}
async function getData() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/home/', {
            'method': 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`
            },
        })
        if (response.status === 401) {
            localStorage.removeItem('token')
            document.location.replace('login/login.html')
            return null
        }
        const data = await response.json()
        user.innerText = data.data.user ? data.data.user + "👋" : "User 👋"
        console.log(data)
        console.log(data.data.user)

    }
    catch (error) {
        document.location.href = 'login/login.html'
    }
}

getData()