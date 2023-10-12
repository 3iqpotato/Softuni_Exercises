SELECT
	t.town_id,
	t.name,
	addresses.address_text
FROM towns as t
JOIN addresses ON t.town_id = addresses.town_id
WHERE t.name LIKE '%San Francisco%' or t.name LIKE '%Sofia%' or t.name LIKE '%Carnation%'

ORDER BY t.town_id, addresses.address_id