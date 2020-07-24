from notion.client import NotionClient
from notion.block import PageBlock
from notion.block import BulletedListBlock

def new_page(parentURL, TITLE):

	# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
	client = NotionClient(token_v2="c02de938cb8e67be2965c739b0f47794b264601edb542c1a844585485ee4c8a460c30896a76bc2ced96c357b2c86ab7bbb853cd9297e598b680d1ef81e630a4f0f9af6d32d6b5b7568a046314a70")

	# Replace this URL with the URL of the page you want to edit
	parentPage = client.get_block(parentURL)


	# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
	page = parentPage.children.add_new(PageBlock, title = TITLE)
	return page

def new_bullet(PAGE,TEXT):

	# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
	client = NotionClient(token_v2="c02de938cb8e67be2965c739b0f47794b264601edb542c1a844585485ee4c8a460c30896a76bc2ced96c357b2c86ab7bbb853cd9297e598b680d1ef81e630a4f0f9af6d32d6b5b7568a046314a70")
	
	# Add new bullet
	bullet = PAGE.children.add_new(BulletedListBlock, title = TEXT)
	return bullet