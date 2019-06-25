function scrollToBottom (scrollSection) {
    var eachScrollSection = document.body.scrollHeight / scrollSection
    var realScrollSection = 0
    var scrollCount = 0
    var timer = setInterval(function() {
        console.log('scrollCount',scrollCount)
        console.log('realScrollSection', realScrollSection)
        realScrollSection += eachScrollSection
        window.scrollTo(0,realScrollSection)
        scrollCount++
        if (scrollCount == scrollSection) clearInterval(timer)
    }, 1000)
}

scrollToBottom(20)