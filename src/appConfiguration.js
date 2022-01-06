/* Home doc */
/**
 * @file Main configuration for the application
 * @see module:appConfiguration
 */

/* Module doc */
/**
 * Main configuration for the application
 * @module appConfiguration
 */


/**
 * App configuration
 * @type {object}
 */
const appConfiguration = Object.freeze({
	locations: [
		{
			id: 3448433, // São Paulo
			timezone: 'America/Sao_Paulo'
		},
		{
			id: 3470127, // Belo Horizonte
			timezone: 'America/Sao_Paulo'
		},
		{
			id: 3451190, // Rio de Janeiro
			timezone: 'America/Sao_Paulo'
		},
		{
			id: 3469058, // Brasília
			timezone: 'America/Sao_Paulo'
		},
		{
			id: 6320062, // Fortaleza
			timezone: 'America/Sao_Paulo'
		},
		{
			id: 3450554, // Salvador
			timezone: 'America/Sao_Paulo'
		},
		{
			id: 3465038, // Cuiabá
			timezone: 'America/Sao_Paulo'
		},
		{
			id: 3390760, // Recife
			timezone: 'America/Sao_Paulo'
		},
		{
			id: 6322752, // Curitiba
			timezone: 'America/Sao_Paulo'
		},
		{
			id: 3452925, // Porto Alegre
			timezone: 'Europe/Madrid'
		},
		{
			id: 6323121, // Florianópolis
			timezone: 'Europe/Madrid'
		},
		{
			id: 3462377, // Goiânia
			timezone: 'Europe/Madrid'
		},
	],
	publishInterval: 1200000 // 1200000 = 20 minutes
});

/** App Configuration */
module.exports = { appConfiguration };


