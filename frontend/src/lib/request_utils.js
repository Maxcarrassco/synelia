const BASE_URL = "http://127.0.0.1:8000/api/v1";

export const getData = async (route) => {
  const url = `${BASE_URL}/${route}/`
  const data = await fetch(url);
  return data;
}


export const postData = async (data, route) => {
  const url = `${BASE_URL}/${route}/`
  const res = await fetch(url, {
      method: "POST",
      headers: {
         'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
  });

  return res;
}
