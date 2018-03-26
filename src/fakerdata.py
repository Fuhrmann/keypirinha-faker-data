# Keypirinha launcher (keypirinha.com)

import keypirinha as kp
import keypirinha_util as kpu
import keypirinha_net as kpnet
import json

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

from faker import Faker

class FakerData(kp.Plugin):

	ITEMCAT = kp.ItemCategory.USER_BASE + 1
	ITEMRESULT = kp.ItemCategory.USER_BASE + 2

	# The default ammount of suggestions to show after the user selected the faker category
	DEFAULT_MAX_RESULTS = 5

	# The default language used to instantiate Faker
	DEFAULT_LANGUAGE = 'en_US'

	def __init__(self):
		super().__init__()
		self.current_output = []

	def on_start(self):
		self.read_config()
		pass

	def on_events(self, flags):
		if flags & kp.Events.PACKCONFIG:
			self.read_config()

	def on_catalog(self):
		self.set_catalog([
			self.create_item(
				category=kp.ItemCategory.KEYWORD,
				label="Faker",
				short_desc="Generate fake data",
				target="Faker",
				args_hint=kp.ItemArgsHint.REQUIRED,
				hit_hint=kp.ItemHitHint.KEEPALL
			)
		])

	def on_suggest(self, user_input, items_chain):
		if not items_chain or items_chain[0].category() != kp.ItemCategory.KEYWORD:
			return

		suggestions = []

		# Generate outputs
		if len(items_chain) == 2:
			items = []
			# We don't want to generate the output each time the user enter a new query
			# Let's keep the output, so this way Keypirinha itself can filter it
			if not self.current_output:
				for x in range(0, self.max_results):
					try:
						items.append(str(getattr(self.fakeGenerator, items_chain[1].target())()))
					except Exception as error:
						items.append(str(error))
						continue

				if len(items) > 0:
					# Remove duplicated
					items = list(set(items))

					# Append suggestions
					for x in items:
						self.current_output.append(
							self.create_item(
								category=self.ITEMRESULT,
								label=x,
								short_desc='Press Enter to copy',
								target=x,
								args_hint=kp.ItemArgsHint.FORBIDDEN,
								hit_hint=kp.ItemHitHint.IGNORE,
								loop_on_suggest=False
							)
						)

			suggestions = self.current_output

		# Generate suggestions categories
		else:
			self.current_output = []
			lines = self.load_text_resource('providers.json')
			data = json.loads(lines)

			for item in data:
				try:
					suggestions.append(
						self.create_item(
							category=self.ITEMCAT,
							label=item['name'],
							short_desc=item['description'],
							target=item['function'],
							args_hint=kp.ItemArgsHint.FORBIDDEN,
							hit_hint=kp.ItemHitHint.IGNORE,
							icon_handle=self.load_icon("res://{}/icons/{}.png".format(self.package_full_name(), item['name'][0].upper())),
							loop_on_suggest=True
						)
					)
				except Exception as error:
					self.err("Could not generate suggestion for fake data category: {}".format(item['name']), error)

		self.set_suggestions(suggestions, kp.Match.FUZZY, kp.Sort.DEFAULT)

	def on_execute(self, item, action):
		if (item.category() == self.ITEMCAT):
			to_clipboard = getattr(self.fakeGenerator, item.target())()
		elif (item.category() == self.ITEMRESULT):
			to_clipboard = item.label()

		kpu.set_clipboard(to_clipboard)

	def read_config(self):
		settings = self.load_settings()
		self.max_results = int(settings.get("max_results", section="main", fallback=self.DEFAULT_MAX_RESULTS))
		self.language = settings.get("language", section="main", fallback=self.DEFAULT_LANGUAGE)
		self.fakeGenerator = Faker(self.language)