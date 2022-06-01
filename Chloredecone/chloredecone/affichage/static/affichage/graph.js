const barCanvas = document.getElementById("barCanvas");
const barChart = new Chart(barCanvas,{
    type: "bar",
    data:{
        labels:["bejinsg","Tokyo","seoule"],
        datasets:[{
            data:[200,100,150]
        }]
    }
})