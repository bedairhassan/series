let series = (string,beginEnd)=>{
  for (let i=beginEnd[0];i<=beginEnd[1];i++){
    console.log(`${string}${i}`)
  }
}

series(`Chapter `,[1,17])
