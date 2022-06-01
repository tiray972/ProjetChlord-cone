const barCanvas = document.getElementById("barCanvas");
function graphique(tritres,donne){
    const barChart = new Chart(barCanvas,{
        type: "bar",
        data:{
            labels:tritres,
            datasets:[{
                data:donne
            }]
        }
    })
}