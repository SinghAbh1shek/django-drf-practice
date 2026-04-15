const token = localStorage.getItem("token");

if (token) {
    window.location.href = "/index.html";
}


const form = document.getElementById('loginForm')

form.addEventListener('submit', async (e) => {
    e.preventDefault()
    const email = document.getElementById("email").value
    const password = document.getElementById('psw').value
    console.log(email)
    console.log(password)

    try {
        const response = await fetch('http://127.0.0.1:8000/api/auth/login/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                email: email,
                password: password
            })
        })
        const data = await response.json()
        if (response.ok) {
            localStorage.setItem("token", data.data['token'])
            alert('login successful')
            window.location.href = '/index.html'
            
        } else {
            alert(data.data['non_field_errors'][0])
            
        }
    }
    catch (error) {
        alert("something went wrong")
    }
        
})