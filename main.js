console.log("Cotton AI Loaded Successfully");

/* =====================================================
   IMAGE UPLOAD PREVIEW (Predict Page)
===================================================== */

const imageInput = document.getElementById("imageInput");
const previewImage = document.getElementById("previewImage");
const resultCard = document.getElementById("resultCard");

if (imageInput && previewImage) {
    imageInput.addEventListener("change", function () {
        const file = this.files[0];
        if (file) {
            previewImage.src = URL.createObjectURL(file);
            previewImage.style.display = "block";
        }
    });
}

/* =====================================================
   AI DISEASE ANALYSIS (Backend Connected)
===================================================== */

function analyzeDisease() {
    const fileInput = document.getElementById("imageInput");
    if (!fileInput || !fileInput.files.length) {
        alert("Please upload an image first");
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("image", file);

    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        body: formData
    })
    .then(res => {
        if (!res.ok) {
            throw new Error("Server error");
        }
        return res.json();
    })
    .then(data => {
        document.getElementById("diseaseName").innerText = data.disease;
        document.getElementById("confidence").innerText = data.confidence + "%";

        const severityEl = document.querySelector(".severity");
        if (severityEl) severityEl.innerText = data.severity;

        const ul = document.querySelector("#resultCard ul");
        if (ul) {
            ul.innerHTML = `
                <li><b>Symptoms:</b> ${data.symptoms}</li>
                <li><b>Prevention:</b> ${data.prevention}</li>
                <li><b>Treatment:</b> ${data.treatment}</li>
            `;
        }

        if (resultCard) {
            resultCard.style.display = "block";
            resultCard.scrollIntoView({ behavior: "smooth" });
        }

        showFutureRisk();
        showWeatherRisk();

        const xai = document.getElementById("xaiSection");
        if (xai) xai.style.display = "block";
    })
    .catch(err => {
        console.error("AI Fetch Error:", err);
    });
}

/* =====================================================
   FUTURE & WEATHER RISK (Predict Page)
===================================================== */

function showFutureRisk() {
    const riskSection = document.getElementById("futureRisk");
    const riskFill = document.getElementById("riskFill");

    if (!riskSection || !riskFill) return;

    riskSection.style.display = "block";
    const riskValue = 63;
    riskFill.style.width = riskValue + "%";
    riskFill.innerText = riskValue + "%";
}

function showWeatherRisk() {
    const weather = document.getElementById("weatherRisk");
    if (weather) weather.style.display = "block";
}

/* =====================================================
   HEALTHY vs DISEASED IMAGE PREVIEW
===================================================== */

const healthyInput = document.getElementById("healthyInput");
if (healthyInput) {
    healthyInput.addEventListener("change", function () {
        const preview = document.getElementById("healthyPreview");
        if (preview && this.files[0]) {
            preview.src = URL.createObjectURL(this.files[0]);
        }
    });
}

const diseasedInput = document.getElementById("diseasedInput");
if (diseasedInput) {
    diseasedInput.addEventListener("change", function () {
        const preview = document.getElementById("diseasedPreview");
        if (preview && this.files[0]) {
            preview.src = URL.createObjectURL(this.files[0]);
        }
    });
}

/* =====================================================
   CONTACT FORM (Contact Page)
===================================================== */

const contactForm = document.getElementById("contactForm");
if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const queryType = document.getElementById("queryType");
        const alertBox = document.getElementById("alertBox");

        if (!queryType || !alertBox) return;

        if (queryType.value === "emergency") {
            alertBox.innerHTML = "🚨 HIGH PRIORITY: Experts will contact you immediately.";
            alertBox.style.color = "red";
        } else {
            alertBox.innerHTML =
                "✅ Query submitted successfully. Reference ID: CA-" +
                Math.floor(Math.random() * 100000);
            alertBox.style.color = "green";
        }
    });
}

/* =====================================================
   DISEASE PAGE ANIMATIONS
===================================================== */

const diseaseCards = document.querySelectorAll(".disease-card");
if (diseaseCards.length > 0) {
    window.addEventListener("scroll", () => {
        diseaseCards.forEach(card => {
            const rect = card.getBoundingClientRect();
            if (rect.top < window.innerHeight - 100) {
                card.style.opacity = "1";
                card.style.transform = "translateY(0)";
            }
        });
    });
}

/* =====================================================
   MODAL (Disease Details)
===================================================== */

const modal = document.getElementById("modal");
const modalBody = document.getElementById("modalBody");

function openModal(type) {
    if (!modal || !modalBody) return;
    modal.style.display = "block";

    if (type === "blight") {
        modalBody.innerHTML = `
            <h2>Bacterial Blight</h2>
            <p><b>Cause:</b> Xanthomonas bacteria</p>
            <p><b>Symptoms:</b> Angular leaf spots</p>
            <p><b>Treatment:</b> Copper fungicide</p>
        `;
    }
}

function closeModal() {
    if (modal) modal.style.display = "none";
}

/* =====================================================
   SEARCH (Disease Page)
===================================================== */

const searchInput = document.getElementById("searchInput");
if (searchInput) {
    searchInput.addEventListener("keyup", e => {
        const value = e.target.value.toLowerCase();
        document.querySelectorAll(".disease-card").forEach(card => {
            card.style.display =
                card.innerText.toLowerCase().includes(value) ? "block" : "none";
        });
    });
}
