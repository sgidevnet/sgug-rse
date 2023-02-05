Name:           vim-jellybeans
Version:        1.7
Release:        2%{?dist}
Summary:        A colorful, dark color scheme for Vim
License:        MIT
URL:            https://github.com/nanotech/jellybeans.vim
Source0:        %{url}/archive/v%{version}/jellybeans.vim-%{version}.tar.gz
# extracted from source code comments
Source1:        LICENSE
BuildArch:      noarch
# for %%vimfiles_root macro
BuildRequires:  vim-filesystem
Requires:       vim-filesystem


%description
A colorful, dark color scheme for Vim.


%prep
%autosetup -n jellybeans.vim-%{version}
cp %{S:1} .


%install
install -D -p -m 644 colors/jellybeans.vim %{buildroot}%{vimfiles_root}/colors/jellybeans.vim


%files
%license LICENSE
%doc README.markdown
%{vimfiles_root}/colors/jellybeans.vim


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Carl George <carl@george.computer> - 1.7-1
- Latest upstream

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Carl George <carl@george.computer> - 1.6-1
- Initial package
