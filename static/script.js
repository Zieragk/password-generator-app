document.getElementById('passwordForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = {
        length: document.getElementById('length').value,
        include_upper: document.getElementById('include_upper').checked,
        include_lower: document.getElementById('include_lower').checked,
        include_digits: document.getElementById('include_digits').checked,
        include_symbols: document.getElementById('include_symbols').checked
    };
    
    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        });
        
        const data = await response.json();
        if (data.error) {
            alert(data.error);
            return;
        }
        
        document.getElementById('generatedPassword').textContent = data.password;
        document.getElementById('result').classList.remove('hidden');
    } catch (error) {
        alert('Error al generar contraseña. Intenta de nuevo.');
    }
});

document.getElementById('copyBtn').addEventListener('click', () => {
    const password = document.getElementById('generatedPassword').textContent;
    navigator.clipboard.writeText(password).then(() => {
        alert('¡Copiada al portapapeles!');
    });
});

document.getElementById('generateAgain').addEventListener('click', () => {
    document.getElementById('passwordForm').dispatchEvent(new Event('submit'));
});