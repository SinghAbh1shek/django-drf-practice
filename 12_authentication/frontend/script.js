// const getData = async () => {
//     const res = await fetch('http://127.0.0.1:8000/api/home/')
//     return  res.json()
// }
// // console.log(getData())

// const result = await getData()
// console.log(result())

// const getData = fetch('http://127.0.0.1:8000/api/home/')
// console.log(getData)


async function getData() {
    const res = await fetch('http://127.0.0.1:8000/api/home/')
    console.log(await res.json())
}
getData()