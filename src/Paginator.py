import disnake
from disnake.ext import commands


class Simple(disnake.ui.View):
    """
    Embed Paginator.

    Parameters:
    ----------
    timeout: int
        How long the Paginator should timeout in, after the last interaction. (In seconds) (Overrides default of 60)
    PreviousButton: disnake.ui.Button
        Overrides default previous button.
    NextButton: disnake.ui.Button
        Overrides default next button.
    PageCounterStyle: disnake.ButtonStyle
        Overrides default page counter style.
    InitialPage: int
        Page to start the pagination on.
    """

    def __init__(self, *,
                 timeout: int = 60,
                 PreviousButton: disnake.ui.Button = disnake.ui.Button(emoji=disnake.PartialEmoji(name="\U000025c0")),
                 NextButton: disnake.ui.Button = disnake.ui.Button(emoji=disnake.PartialEmoji(name="\U000025b6")),
                 PageCounterStyle: disnake.ButtonStyle = disnake.ButtonStyle.grey,
                 InitialPage: int = 0) -> None:
        self.PreviousButton = PreviousButton
        self.NextButton = NextButton
        self.PageCounterStyle = PageCounterStyle
        self.InitialPage = InitialPage

        self.pages = None
        self.ctx = None
        self.message = None
        self.current_page = None
        self.page_counter = None
        self.total_page_count = None

        super().__init__(timeout=timeout)

    async def start(self, ctx: commands.Context, pages: list[disnake.Embed]):
        self.pages = pages
        self.total_page_count = len(pages)
        self.ctx = ctx
        self.current_page = self.InitialPage

        self.PreviousButton.callback = self.previous_button_callback
        self.NextButton.callback = self.next_button_callback

        self.page_counter = SimplePaginatorPageCounter(style=self.PageCounterStyle,
                                                       TotalPages=self.total_page_count,
                                                       InitialPage=self.InitialPage)

        self.add_item(self.PreviousButton)
        self.add_item(self.page_counter)
        self.add_item(self.NextButton)

        self.message = await ctx.send(embed=self.pages[self.InitialPage], view=self)

    async def previous(self):
        if self.current_page == 0:
            self.current_page = self.total_page_count - 1
        else:
            self.current_page -= 1

        self.page_counter.label = f"{self.current_page + 1}/{self.total_page_count}"
        await self.message.edit(embed=self.pages[self.current_page], view=self)

    async def next(self):
        if self.current_page == self.total_page_count - 1:
            self.current_page = 0
        else:
            self.current_page += 1

        self.page_counter.label = f"{self.current_page + 1}/{self.total_page_count}"
        await self.message.edit(embed=self.pages[self.current_page], view=self)

    async def next_button_callback(self, interaction: disnake.Interaction):
        if interaction.user != self.ctx.author:
            embed = disnake.Embed(description="You cannot control this pagination because you did not execute it.",
                                  color=disnake.Colour.red())
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.response.defer()
        await self.next()

    async def previous_button_callback(self, interaction: disnake.Interaction):
        if interaction.user != self.ctx.author:
            embed = disnake.Embed(description="You cannot control this pagination because you did not execute it.",
                                  color=disnake.Colour.red())
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.response.defer()
        await self.previous()


class SimplePaginatorPageCounter(disnake.ui.Button):
    def __init__(self, style: disnake.ButtonStyle, TotalPages, InitialPage):
        super().__init__(label=f"{InitialPage + 1}/{TotalPages}", style=style, disabled=True)
