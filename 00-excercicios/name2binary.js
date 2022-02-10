Array.from('rodrigorogovski')
.reduce((acc, curr, idx) => acc += `${idx > 0 ? ' 0' : '0'}` + curr.charCodeAt(0).toString(2),'') 
