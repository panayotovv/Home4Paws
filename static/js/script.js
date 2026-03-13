document.addEventListener("DOMContentLoaded", () => {

    const menuBtn = document.querySelector(".menu-toggle");
    const nav = document.querySelector("nav");
    const modal = document.querySelector(".auth-modal");
    const signInForm = document.querySelector(".sign-in-form");
    const signUpForm = document.querySelector(".sign-up-form");
    const switchToSignup = document.querySelector(".switch-to-signup");
    const switchToSignin = document.querySelector(".switch-to-signin");
    const infoModal = document.querySelector(".info-modal");
    const infoTitle = document.querySelector(".info-title");
    const infoContent = document.querySelector(".info-content");
    const profileModal = document.querySelector(".profile-modal");
    const editProfileBtn = document.querySelector(".edit-profile-btn");
    const searchInput = document.querySelector(".pet-search");
    const cards = document.querySelectorAll(".animals a");
    const animalsBox = document.querySelector(".animals");
    const closeBtns = document.querySelectorAll(".close-info");
    const dogCount = document.querySelector(".dog-count");
    const adoptBtn = document.querySelector(".adopt-btn");
    const adoptModal = document.querySelector(".adopt-modal");
    const amountButtons = document.querySelectorAll(".amount-btn");
    const amountInput = document.getElementById("custom-amount");
    const langToggle = document.getElementById("langToggle");
    const langMenu = document.getElementById("langMenu");

    function initObserver() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) entry.target.classList.add("show");
            });
        }, { threshold: 0.2 });

        document.querySelectorAll(".reveal").forEach(el => {
            el.classList.remove("show");
            observer.observe(el);
        });
    }

    window.addEventListener("pageshow", initObserver);
    window.history.scrollRestoration = "manual";
    window.addEventListener("load", () => window.scrollTo(0, 0));

    menuBtn?.addEventListener("click", (e) => {
        e.stopPropagation();
        nav.classList.add("active");
        menuBtn.classList.add("hidden");
    });

    document.addEventListener("click", (e) => {
        if (nav && !nav.contains(e.target)) {
            nav.classList.remove("active");
            menuBtn?.classList.remove("hidden");
        }
        if (langMenu && !e.target.closest(".lang-switcher")) {
            langMenu.classList.remove("open");
        }
    });

    function toggleAuthModal(showSignIn) {
        modal?.classList.add("active");
        document.body.classList.add("modal-open");
        signInForm?.classList.toggle("active-form", showSignIn);
        signUpForm?.classList.toggle("active-form", !showSignIn);
    }

    document.querySelector(".sign-in-btn")?.addEventListener("click", () => toggleAuthModal(true));
    document.querySelector(".sign-up-btn")?.addEventListener("click", () => toggleAuthModal(false));
    switchToSignup?.addEventListener("click", () => toggleAuthModal(false));
    switchToSignin?.addEventListener("click", () => toggleAuthModal(true));

    function openInfoModal(title, text) {
        if (!infoModal) return;
        infoTitle.textContent = title;
        infoContent.textContent = text;
        infoModal.classList.add("active");
    }

    document.querySelectorAll(".about-link").forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            openInfoModal(
                "About Us",
                "We rescue, care for, and rehome dogs who are searching for loving families and a second chance at happiness. Our mission is to provide safe shelter, proper medical care, and plenty of affection while we help each dog find a permanent home."
            );
        });
    });

    document.querySelectorAll(".contact-link").forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            openInfoModal(
                "Contact Us",
                "If you have questions about adoption, volunteering, or supporting our mission, feel free to contact us. Email us at support@home4paws.com."
            );
        });
    });

    infoModal?.addEventListener("click", (e) => {
        e.stopPropagation();
        if (e.target === infoModal) infoModal.classList.remove("active");
    });

    closeBtns.forEach(btn => {
        btn.addEventListener("click", (e) => {
            e.stopPropagation();
            document.body.classList.remove("modal-open");
            [modal, infoModal, profileModal].forEach(m => m?.classList.remove("active"));
            setTimeout(() => {
                signUpForm?.classList.remove("active-form");
                signInForm?.classList.remove("active-form");
            }, 300);
        });
    });

    searchInput?.addEventListener("input", () => {
        const query = searchInput.value.toLowerCase().trim();
        cards.forEach(card => {
            const matches = [...card.querySelectorAll("h3")].some(el =>
                el.textContent.toLowerCase().includes(query)
            );
            card.classList.toggle("hidden", !matches);
            if (matches) card.classList.add("show");
        });
    });

    editProfileBtn?.addEventListener("click", () => profileModal?.classList.add("active"));


    const successModal = document.getElementById("successModal")
    const closeProfileBtns = document.querySelectorAll(".close-profile")

    closeProfileBtns.forEach(btn => {
        btn.addEventListener("click", (e) => {
            e.stopPropagation();
            profileModal?.classList.remove("active");
            adoptModal?.classList.remove("active");
            successModal?.classList.remove("active");
        })
    })
    // profileModal?.addEventListener("click", (e) => {
    //     if (e.target === profileModal) profileModal.classList.remove("active");
    // });

    // modal?.addEventListener("click", (e) => {
    //     if (e.target === modal) {
    //         modal.classList.remove("active");
    //         document.body.classList.remove("modal-open");
    //     }
    // });

    adoptBtn?.addEventListener("click", () => adoptModal?.classList.add("active"));

    // adoptModal?.addEventListener("click", (e) => {
    //     if (e.target === adoptModal) adoptModal.classList.remove("active");
    // });

    if (dogCount && animalsBox) {
        const hasAnimals = Number(dogCount.textContent) > 0;
        animalsBox.classList.toggle("animals", hasAnimals);
        animalsBox.classList.toggle("no-animals", !hasAnimals);
    }

    amountButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            amountButtons.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            if (amountInput) amountInput.value = btn.dataset.amount;
        });
    });


    document.getElementById("id_image")?.addEventListener("change", function () {
        document.getElementById("avatarForm").submit();
    });

    function applyGoogleTranslate(lang) {
        const select = document.querySelector(".goog-te-combo");
        if (select) {
            select.value = lang;
            select.dispatchEvent(new Event("change"));
        } else {
            setTimeout(() => applyGoogleTranslate(lang), 300);
        }
    }

    const savedLang = localStorage.getItem("selectedLang");
    if (savedLang && savedLang !== "en") {
        const currentLang = document.getElementById("currentLang");
        if (currentLang) currentLang.textContent = savedLang.toUpperCase();
        setTimeout(() => applyGoogleTranslate(savedLang), 1000);
    }

    langToggle?.addEventListener("click", (e) => {
        e.stopPropagation();
        langMenu.classList.toggle("open");
    });

    document.querySelectorAll(".lang-menu button[data-lang]").forEach(btn => {
        btn.addEventListener("click", (e) => {
            e.preventDefault();
            e.stopPropagation();
            const lang = btn.dataset.lang;
            const currentLang = document.getElementById("currentLang");
            if (currentLang) currentLang.textContent = lang.toUpperCase();
            langMenu.classList.remove("open");
            localStorage.setItem("selectedLang", lang);
            applyGoogleTranslate(lang);
        });
    });

    const cardElement = document.getElementById("card-element");

    if (cardElement) {

        const stripe = Stripe(STRIPE_PUBLIC_KEY);

        const elements = stripe.elements();
        const card = elements.create("card");

        card.mount("#card-element");

        const donateBtn = document.getElementById("donate-btn");

        donateBtn?.addEventListener("click", async () => {
            console.log("Donate button clicked");

            const response = await fetch("/user/create-payment-intent/", {
                method: "POST",
            });

            const data = await response.json();

            const result = await stripe.confirmCardPayment(data.clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: document.getElementById("card-name").value
                    }
                }
            });

            if (result.error) {
                document.getElementById("card-errors").textContent = result.error.message;
            } else {
                const successModal = document.getElementById("donationSuccess");

                successModal.classList.add("active");

                setTimeout(() => {
                    window.location.href = "/";
                }, 2500);
            }

        });

    }
    const adoptBtnn = document.getElementById('adoptBtn')
    if (adoptBtnn) {
        adoptBtnn.addEventListener('click', () => {
            document.querySelector(".auth-modal").classList.add("active");
            document.querySelector(".sign-in-form").classList.add("active-form");
        })
    }

});