disnake-pagination

#### disnake-pagination is a Python library to easily create embed paginators.

## Installation

```bash
pip install git+https://github.com/SlumberDemon/disnake-Pagination
```

## Usage

### Quickstart
```python
import Paginator

# Create a list of embeds to paginate.
embeds = [disnake.Embed(title="First embed"),
          disnake.Embed(title="Second embed"),
          disnake.Embed(title="Third embed")]

... # Inside a command.
await Paginator.Simple().start(ctx, pages=embeds)
```

### Advanced

##### To use custom buttons, pass in the corresponding argument when you initiate the paginator.

```python
# These arguments override the default ones.

PreviousButton = disnake.ui.Button(...)
NextButton = disnake.ui.Button(...)
PageCounterStyle = disnake.ButtonStyle(...) # Only accepts ButtonStyle instead of Button
InitialPage = 0 # Page to start the paginator on.
timeout = 42069 # Seconds to timeout. Default is 60

await Paginator.Simple(
    PreviousButton=PreviousButton,
    NextButton=NextButton,
    PageCounterStyle=PageCounterStyle,
    InitialPage=InitialPage,
    timeout=timeout).start(ctx, pages=embeds)
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
