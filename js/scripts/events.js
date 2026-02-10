function switchEvents(type) {
    console.log("Switching to: " + type);
    // 1. Selectăm elementele
    const btnOrg = document.getElementById('tab-btn-organized');
    const btnAtt = document.getElementById('tab-btn-attendance');
    
    const contentOrg = document.getElementById('content-organized');
    const contentAtt = document.getElementById('content-attendance');

    if (type === 'organized') {
        // Arătăm conținutul Organized
        contentOrg.style.display = 'block';
        contentAtt.style.display = 'none';

        // Butonul Organized devine SOLID (Activ)
        btnOrg.className = "btn-solid btn-medium";
        
        // Butonul Attendance devine OUTLINE (Inactiv)
        btnAtt.className = "btn-outline btn-medium";
        
        // Resetăm stilul inline pentru margine
        btnAtt.style.marginLeft = "15px"; 
        btnOrg.style.marginRight = "0px";

    } else {
        // Arătăm conținutul Attendance
        contentOrg.style.display = 'none';
        contentAtt.style.display = 'block';

        // Butonul Organized devine OUTLINE (Inactiv)
        btnOrg.className = "btn-outline btn-medium";
        
        // Butonul Attendance devine SOLID (Activ)
        btnAtt.className = "btn-solid btn-medium";
        
        // Ajustăm marginea ca să arate bine spațierea
        btnOrg.style.marginRight = "15px";
        btnAtt.style.marginLeft = "0px";
    }
}