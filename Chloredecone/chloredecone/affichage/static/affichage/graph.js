const barCanvas = document.getElementById("barCanvas");
function graphique(tritres,donne){
    const barChart = new Chart(barCanvas,{
        type: "bar",
        data:{
            labels:tritres,
            datasets:[{
                data:donne,
                backgroundColor:[
                    "crimson",
                    "lightgreen",
                    "lightblue",
                    "violet"
                ]

            }]
        }
    })
};
const pieCanvas = document.getElementById("pieCanvas");
function graphiquecam(tritres,donne){
    const pieChart = new Chart(pieCanvas,{
        type: "pie",
        data:{
            labels:tritres,
            datasets:[{
                data:donne,
                backgroundColor:[
                    "crimson",
                    "lightgreen",
                    "lightblue",
                    "violet"
                ]

            }]
        }
    })
}