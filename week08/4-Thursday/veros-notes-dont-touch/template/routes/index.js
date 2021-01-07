
const express = require('express');
const router = express.Router();

let pictures = [
    "https://i.pinimg.com/originals/f4/01/0b/f4010b762ef1cd617f5e9a0a8ca0533a.jpg",
    "https://cdn.hpm.io/wp-content/uploads/2016/10/07162709/IMG_5206.jpg",
    "https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/houston-skyline-from-above-tod-and-cynthia-grubbs.jpg"
]

let nameArr = [
    "Woody",
    "RJ",
    "Micah",
    "Jeremy",
    "Chris",
    "Dan",
    "Cainan",
    "Michael"
]

let cities = [
    "Atlanta",
    "Houston",
    "Seattle",
    "Miami"
]

router.get('/', (req, res) => {

    res.render('index', {
        pic: pictures
    })

    // res.render('index', {
    //     pic1: pictures[0],
    //     pic2: pictures[1],
    //     pic3: pictures[2],
    //     Atlanta: cities[0],
    //     Houston: cities[1],
    //     Seattle: cities[2],


    // })
    
    // res.render('index', {
    //     firstName: "Michael",
    //     lastName: "Jackson"

    // })   
})

router.get('/:id', (req, res) => {
  
    let id = req.params.id;
    res.render('index', {
        pic: pictures[id]
    })
})



module.exports = router;



