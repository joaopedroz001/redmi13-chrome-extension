const body = document.body

async function getData() {
	try {
		const reply = await fetch('data.json')
		const data = await reply.json()

		return data
	} catch (error) {
		console.error(error)
	}
}

getData().then(data => {
	data.forEach(card => (
		body.innerHTML += `
			<a href="${card.link}" target="_blank" class="card">
				<div class="card_main">
					<div class="card_site-logo">
						<img src="${card.img}" alt="Amazon logo" width="20px" height="20px">
						<span class="card_site-title">${card.name}</span>
					</div>
						<span class="card_price">${card.price}</span>
					</div>
				<span class="card_description">${card.description}</span>
			</a>
			`
	))
})