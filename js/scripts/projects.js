function switchEvents(type) {
    console.log("Switching to: " + type);
    // 1. Selectăm elementele
    const btnOrg = document.getElementById('tab-btn-ongoing');
    const btnAtt = document.getElementById('tab-btn-completed');
    
    const contentOrg = document.getElementById('content-ongoing');
    const contentAtt = document.getElementById('content-completed');

    if (type === 'ongoing') {
        contentOrg.style.display = 'block';
        contentAtt.style.display = 'none';

        btnOrg.className = "btn-solid btn-medium";
        
        btnAtt.className = "btn-outline btn-medium";
        
        btnAtt.style.marginLeft = "15px"; 
        btnOrg.style.marginRight = "0px";

    } else {
        contentOrg.style.display = 'none';
        contentAtt.style.display = 'block';

        btnOrg.className = "btn-outline btn-medium";
        
        btnAtt.className = "btn-solid btn-medium";
        
        btnOrg.style.marginRight = "15px";
        btnAtt.style.marginLeft = "0px";
    }
}