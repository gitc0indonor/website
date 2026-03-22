<?php
// Enqueue Google Fonts for Cormorant Garamond
add_action( 'wp_enqueue_scripts', 'cognivia_enqueue_fonts' );
function cognivia_enqueue_fonts() {
    wp_enqueue_style( 'cognivia-google-fonts', 'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&display=swap', array(), null );
}

// Add custom body classes if needed
add_filter( 'body_class', 'cognivia_body_classes' );
function cognivia_body_classes( $classes ) {
    $classes[] = 'cognivia-site';
    return $classes;
}
