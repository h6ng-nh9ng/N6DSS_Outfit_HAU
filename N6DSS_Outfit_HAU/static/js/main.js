document.addEventListener('DOMContentLoaded', function () {
    // 1. Xử lý chọn Hoạt động (Màn 1)
    const activityCards = document.querySelectorAll('.activity-card');
    const btnContinue = document.getElementById('btnContinue');
    const actionHint = document.getElementById('actionHint');
    let selectedActivity = null;

    activityCards.forEach(card => {
        card.addEventListener('click', function () {
            activityCards.forEach(c => c.classList.remove('selected'));
            this.classList.add('selected');
            selectedActivity = this.getAttribute('data-activity');

            if (btnContinue) {
                btnContinue.removeAttribute('disabled');
                btnContinue.classList.add('active');
            }

            if (actionHint) {
                actionHint.textContent = 'Đã chọn hoạt động! Nhấn Tiếp tục để chọn phong cách.';
                actionHint.style.color = '#7C3AED';
            }
        });
    });

    if (btnContinue) {
        btnContinue.addEventListener('click', function () {
            if (selectedActivity) {
                window.location.href = '/style?activity=' + selectedActivity;
            }
        });
    }

    // 2. Xử lý chọn Phong cách & Màu sắc (Màn 2)
    const chipItems = document.querySelectorAll('.chip-item');
    chipItems.forEach(chip => {
        chip.addEventListener('click', function () {
            this.classList.toggle('selected');
            const checkbox = this.querySelector('input[type="checkbox"]');
            if (checkbox) checkbox.checked = this.classList.contains('selected');
        });
    });

    const colorDots = document.querySelectorAll('.color-dot');
    colorDots.forEach(dot => {
        dot.addEventListener('click', function () {
            this.classList.toggle('selected');
            const checkbox = this.querySelector('input[type="checkbox"]');
            if (checkbox) {
                checkbox.checked = this.classList.contains('selected');
                this.textContent = checkbox.checked ? '✓' : '';
            }
        });
    });

    // 3. Xử lý Thanh Slider Mức độ thoải mái (Màn 2)
    const comfortRange = document.getElementById('comfortRange');
    const rangePercent = document.getElementById('rangePercent');

    if (comfortRange && rangePercent) {
        comfortRange.addEventListener('input', function () {
            rangePercent.textContent = this.value + '%';
        });
    }
});