let profile_id = window.location.href.match(/\/([^\/]*)$/)[1]

var map = L.map('map').setView([40, 15], 2);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 2,
    minZoom: 2,
    boxZoom: false,
    zoomControl: false,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
// var marker = L.marker([51.5, -0.09]).addTo(map);

async function getCoutries(type, profile_id) {
    let data = await fetch(`../api/${type}/${profile_id}`)
    let dataJson = await data.json()
    return dataJson
}

async function getSurroundings(profile_id) {
    let data = await fetch('../../static/accounts/app/archive/countries.geojson')
    let dataJson = await data.json()

    let countries = await getCoutries("get_trips", profile_id)
    let country_origin = await getCoutries("get_origin", profile_id)
    console.log(country_origin)

    let selectedCountries = dataJson.features.filter(country => countries['countries'].includes(country.properties.ADMIN))
    let surroundings = {...dataJson, features: selectedCountries}
    
    let selectedOrigin = dataJson.features.filter(country => country_origin.country == country.properties.ADMIN)
    let surroundingsOrigin = {...dataJson, features: selectedOrigin}

    L.geoJson(surroundings).addTo(map)
    L.geoJson(surroundingsOrigin, {color: 'red'}).addTo(map)
}

getSurroundings(profile_id)