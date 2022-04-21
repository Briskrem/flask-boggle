
let result = '';
let score = 0;
let statistics = {
    highestScore: 0
}

$('.form-submit button').hide()

$('.form-submit').on('submit', req)


async function req(e){
    e.preventDefault()
    console.log($('input[name="guess"]').val())
    let word = $('input[name="guess"]').val()

    const rep = await axios({
        url: `/check`,
        method: 'GET',
        params: {'word': word}
    })

    console.log(rep)
    result = rep.data.result

    if (rep.data.result === "ok"){
        console.log(word)
        points = word.length
        console.log('points: ' + points)
        score += points
        console.log('score: ' + score)
        updateScore(score)
    }
    
    $(".wordValidity").text(`Word Validity: ${rep.data.result}`)
    $('input[name="guess"]').val('') 
}

function updateScore(score){
    $('.score').text(`score: ${score}`)
}

$('.begin button').on('click', beginGame)

function beginGame(){
    $('.begin button').hide() 
    $('.form-submit button').show()
    setTimeout(() => {
        console.log("GAME OVER")
        $('.form-submit button').hide()
        statistics.highestScore = score
        makePost()
        
        }, 60000);
    
}

async function makePost(){
    
    req = await axios({
        url: '/storage',
        method: 'POST',
        data: {  'Highscore': statistics.highestScore}
    })
    
    console.log(req)
    await window.location.reload();
}