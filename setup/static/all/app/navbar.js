const profile = document.querySelector('.profile')
const profileWindow = document.querySelector('.profile-window')

profile.addEventListener('mouseover', e => {
    console.log(e)
    profileWindow.setAttribute('style', 'display: block')
})

profile.addEventListener('mouseout', e => {
    profileWindow.setAttribute('style', 'display: none')
})