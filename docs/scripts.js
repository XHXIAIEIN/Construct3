document.addEventListener("DOMContentLoaded", function() {
    fetch('data.json')
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');

            const lastUpdated = document.querySelector('time');
            lastUpdated.textContent = data.lastUpdated;

            const navigate = document.getElementById('navigate');
            const editorNav = data.navigation.editor?.map(item => `<a href="${item.link}" title="${item.name}">${item.name}</a>`).join(' | ') || '';
            const manualsNav = data.navigation.manuals?.map(item => `<a href="${item.link}" title="${item.name}">${item.name}</a>`).join(' | ') || '';
            const cheatsheetNav = data.navigation.cheatsheet?.map(item => `<a href="${item.link}" title="${item.name}">${item.name}</a>`).join(' | ') || '';

            navigate.innerHTML = `
                ${editorNav}
                ${manualsNav}
                ${cheatsheetNav}
            `;

            const fragment = document.createDocumentFragment();

            Object.entries(data.example).forEach(([sectionName, section]) => {
                const sectionDiv = document.createElement('div');
                sectionDiv.className = 'section';

                const sectionTitle = document.createElement('div');
                sectionTitle.className = 'section-title';
                sectionTitle.innerHTML = sectionName;
                sectionDiv.appendChild(sectionTitle);

                Object.entries(section).forEach(([categoryName, category]) => {
                    const categoryDiv = document.createElement('div');
                    categoryDiv.className = 'category';

                    if (categoryName !== sectionName || category.icon) {
                        const categoryTitle = document.createElement('div');
                        categoryTitle.className = 'category-title';
                        categoryTitle.innerHTML = category.icon ? `<img src="svg/${category.icon}" class="category-icon"> ${categoryName}` : categoryName;
                        categoryDiv.appendChild(categoryTitle);
                    }

                    category.data.forEach(item => {
                        try {
                            const itemDiv = document.createElement('div');
                            itemDiv.className = 'item';

                            const itemTitle = document.createElement('div');
                            itemTitle.className = 'item-title';
                            itemTitle.innerHTML = `<a href="${item.link}" class="item-link">${item.title}</a>`;
                            itemDiv.appendChild(itemTitle);

                            const itemAuthors = document.createElement('div');
                            itemAuthors.className = 'item-authors';
                            itemAuthors.innerHTML = `作者: ${item.authors.join(', ')}`;
                            itemDiv.appendChild(itemAuthors);

                            if (item.related_links && item.related_links.length > 0) {
                                const relatedLinksDiv = document.createElement('div');
                                relatedLinksDiv.className = 'item-related-links';
                                relatedLinksDiv.innerHTML = item.related_links.map(link => `<a href="${link}">相关链接</a>`).join(' ');
                                itemDiv.appendChild(relatedLinksDiv);
                            }

                            categoryDiv.appendChild(itemDiv);
                        } catch (e) {
                            console.error('Error processing item:', item, e);
                        }
                    });

                    sectionDiv.appendChild(categoryDiv);
                });

                fragment.appendChild(sectionDiv);
            });

            content.appendChild(fragment);
        })
        .catch(error => console.error('Error loading data:', error));
});
