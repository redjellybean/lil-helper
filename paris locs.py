import pandas as pd

# Data
locations = [
    ["hotelF1 Paris Porte de Châtillon", 48.8225, 2.3136],
    ["Bibliothèque Nationale de France - Richelieu", 48.8686, 2.3385],
    ["La Belle Hortense", 48.8575, 2.3580],
    ["Musée de l'Orangerie", 48.8638, 2.3226],
    ["Eiffel Tower", 48.8584, 2.2945],
    ["L'As du Fallafel", 48.8570, 2.3590],
    ["Louise Café", 48.8530, 2.3370],
    ["Dumbo", 48.8710, 2.3430],
    ["Chez Alain Miam Miam", 48.8625, 2.3600],
    ["Le Bistro Marbeuf", 48.8670, 2.3030],
    ["Hôtel des Invalides", 48.8566, 2.3126],
    ["Jardin du Luxembourg", 48.8462, 2.3372],
    ["Arc de Triomphe", 48.8738, 2.2950],
    ["The Basilica of the Sacred Heart of Paris (Sacré-Cœur)", 48.8867, 2.3431],
    ["Galerie Butte Montmartre", 48.8860, 2.3400],
    ["Montmartre", 48.8867, 2.3431],
    ["Galeries Lafayette Haussmann", 48.8738, 2.3320],
    ["Palais Garnier", 48.8718, 2.3316],
    ["Sainte-Chapelle", 48.8554, 2.3445],
    ["Boutique of the French Comédie", 48.8640, 2.3340],
    ["tucked friperie", 48.8610, 2.3660],
    ["Untucked friperie", 48.8580, 2.3700],
    ["Episode", 48.8615, 2.3520],
    ["Le Procope", 48.8535, 2.3380],
    ["Chinemachine", 48.8865, 2.3405],
    ["Notre Dame", 48.8529, 2.3508],
    ["Shakespeare and Company", 48.8526, 2.3470],
    ["Café Kitsuné Louvre", 48.8635, 2.3370],
    ["Palace of Versailles", 48.8049, 2.1204],
    ["Bontemps La Pâtisserie", 48.8570, 2.3605],
    ["Yann Couvreur Rosiers", 48.8575, 2.3600],
    ["Boulangerie Utopie", 48.8640, 2.3700],
    ["Des Gâteaux et du Pain", 48.8500, 2.3250],
    ["Fou de Pâtisserie", 48.8615, 2.3525],
    ["L'Eclair de Génie Café", 48.8670, 2.3080],
    ["La Meringaie Martyrs", 48.8790, 2.3400],
    ["Pierre Hermé", 48.8660, 2.3110],
    ["Cedric Grolet Café", 48.8700, 2.3300],
    ["Stohrer", 48.8620, 2.3470],
    ["BO&MIE", 48.8610, 2.3500],
    ["Ritz Paris Le Comptoir", 48.8680, 2.3280],
    ["Chapon et la Chocolaterie de l'Eglise", 48.8505, 2.3300],
    ["Le Train Bleu", 48.8440, 2.3740],
    ["Plaza Athénée", 48.8660, 2.3040],
    ["La Poule au Pot", 48.8610, 2.3510],
    ["Bistrot Paul Bert", 48.8540, 2.3800],
]

# Create DataFrame
df = pd.DataFrame(locations, columns=["Place", "Latitude", "Longitude"])

# Save as CSV
file_path = "./Paris_Locations.csv"
df.to_csv(file_path, index=False)

file_path
