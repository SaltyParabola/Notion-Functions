from notion.client import NotionClient
from notion.block import PageBlock
from notion.block import BulletedListBlock

def new_page(parentURL, TITLE):

	# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
	client = NotionClient(token_v2=<TOKEN FROM COOKIES>)

	# Replace this URL with the URL of the page you want to edit
	parentPage = client.get_block(parentURL)


	# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
	page = parentPage.children.add_new(PageBlock, title = TITLE)
	return page

def new_bullet(PAGE,TEXT):

	# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
	client = NotionClient(token_v2=TOKEN FROM COOKIES)
	
	# Add new bullet
	bullet = PAGE.children.add_new(BulletedListBlock, title = TEXT)
	return bullet
