# travel_data.py - Paris Edition (Expanded 12-Spot Version with Original Image URLs)
# MAKE SURE THE IMAGE URL IS VALID

TRAVEL_DATABASE = {
    "funny": [
        {
            "place": "A Crowded Metro Line 13 Car", 
            "desc": "Forget the Eiffel Tower! True Parisian life is being squeezed like a sardine in a metro car at 8:30 AM. Hold your breath and mind your pockets!", 
            "img": "https://images.unsplash.com/photo-1667818027944-fe5424723d1f?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "url": "https://www.ratp.fr/en/plans-lignes/metro/13"
        },
        {
            "place": "A €12 Espresso at a Tourist Cafe", 
            "desc": "Enjoy the 'authentic' experience of sitting on a tiny chair, paying too much for coffee, and being completely ignored by a grumpy waiter.", 
            "img": "https://plus.unsplash.com/premium_photo-1718285552806-5edc34f48d17?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "url": "https://www.google.com/maps"
        },
        {
            "place": "A Bench watching Pigeons at Les Halles", 
            "desc": "When you have no money and no energy left, just sit down and share some breadcrumbs with your new feathered, aggressive friends.", 
            "img": "https://images.unsplash.com/photo-1682939037029-7d4ce224abbf?q=80&w=983&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "url": "https://www.paris.fr/lieux/forum-des-halles-1845"
        },
        {
            "place": "The Arc de Triomphe Chaos", 
            "desc": "Stand at the edge of the world's most hectic roundabout. Watch 12 avenues merge into one crazy circle with zero lane markings, and witness drivers questioning life.", 
            "img": "https://images.unsplash.com/photo-1723101173456-0d1d2801dd27?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "url": "https://www.paris-arc-de-triomphe.fr/en/"
        },
        {
            "place": "The Paris Catacombs", 
            "desc": "Tired of living Parisians judging your French pronunciation? Go 20 meters underground to hang out with 6 million former locals. They are excellent, quiet listeners.", 
            "img": "https://images.unsplash.com/photo-1613469425754-bf71d7280f65?q=80&w=1064&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "url": "https://www.catacombes.paris.fr/en"
        },
        {
            "place": "Trocadéro Pigeon Swarm", 
            "desc": "You wanted a beautiful, aesthetic photo holding a croissant with the Eiffel Tower. Instead, you are now sprinting away from 50 pigeons who claimed your breakfast.", 
            "img": "https://images.unsplash.com/photo-1641144355850-e7991d050bdc?q=80&w=1481&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "url": "https://www.parisinfo.com/"
        }
    ],
    "serious": [
        {
            "place": "The Eiffel Tower at Night", 
            "desc": "Witness the Iron Lady sparkling every hour. It's cliché, but it's pure magic and romance every single time.", 
            "img": "https://images.unsplash.com/photo-1639519307979-b96102a07650?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "url": "https://www.toureiffel.paris/en"
        },
        {
            "place": "The Louvre Museum", 
            "desc": "Spend your day lost in art history. Even if you only manage to see the Mona Lisa's forehead through the crowd of smartphones, it's worth it.", 
            "img": "https://images.unsplash.com/photo-1586168078184-1fe44f2491e1?q=80&w=1064&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "url": "https://www.louvre.fr/en"
        },
        {
            "place": "Montmartre & Sacré-Cœur", 
            "desc": "Climb the beautiful winding hills for the best panoramic view of the city. Art, street music, and a heavy workout for your legs!", 
            "img": "https://images.unsplash.com/photo-1682372249522-6e827e57e818?q=80&w=985&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "url": "https://www.sacre-coeur-montmartre.fr/english/"
        },
        {
            "place": "Sainte-Chapelle", 
            "desc": "Step inside a Gothic jewel box. On a sunny afternoon, the 15-meter high stained glass windows fill the entire chapel with an otherworldly shimmering light.", 
            "img": "https://images.unsplash.com/photo-1590499638699-f01965a739c7?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "url": "https://www.sainte-chapelle.fr/en"
        },
        {
            "place": "Musée de l'Orangerie", 
            "desc": "Sit in the quiet, oval-shaped rooms designed specifically to house Claude Monet’s massive 'Water Lilies' masterpieces. The ultimate peaceful escape.", 
            "img": "https://images.unsplash.com/photo-1629998265896-7634e8b654cf?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "url": "https://www.musee-orangerie.fr/en"
        },
        {
            "place": "Square du Vert-Galant", 
            "desc": "Sit at the very tip of Île de la Cité island, right on the water level of the Seine. Bring wine, cheese, and watch the boats cruise past under the golden sunset.", 
            "img": "https://plus.unsplash.com/premium_photo-1718285549233-42414e1c16f9?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "url": "https://www.paris.fr/lieux/square-du-vert-galant-2748"
        }
    ]
}