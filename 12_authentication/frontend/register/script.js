const token = localStorage.getItem('token')
if (token) {
    window.location.href = '/index.html'
}

form = document.getElementById('signupForm')

form.addEventListener('submit', async (e)=> {
    e.preventDefault()
    const first_name = document.getElementById('fname').value
    const last_name = document.getElementById('lname').value
    const username = document.getElementById('uname').value
    const email = document.getElementById('email').value
    const password = document.getElementById('psw').value

    try {
        response = await fetch('http://127.0.0.1:8000/api/auth/register/', {
            method:'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                first_name: first_name,
                last_name: last_name,
                username: username,
                email: email,
                password: password
            })
        })
        const data = await response.json()

        if(response.ok) {
            localStorage.setItem('token', data.data['token'])
            alert(data.message)
            window.location.href='/index.html'
        } else {
            console.log(data)
            alert(data.message)
        }
    }
    catch (error) {
        console.log(error)
        alert('something went wrong')
    }


})
