%global commit 85ba8277a6e331a56fce920d62bfdacce5bc5a80
%global commitdate 20180615
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           vim-toml
Version:        0
Release:        0.5.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Vim syntax for TOML
License:        MIT
URL:            https://github.com/cespare/vim-toml
Source0:        %{url}/archive/%{commit}/vim-toml-%{shortcommit}.tar.gz
BuildArch:      noarch
# for %%vimfiles_root macro
BuildRequires:  vim-filesystem
Requires:       vim-filesystem


%description
%{summary}.


%prep
%autosetup -n vim-toml-%{commit}


%install
install -D -p -m 644 ftdetect/toml.vim %{buildroot}%{vimfiles_root}/ftdetect/toml.vim
install -D -p -m 644 ftplugin/toml.vim %{buildroot}%{vimfiles_root}/ftplugin/toml.vim
install -D -p -m 644 syntax/toml.vim %{buildroot}%{vimfiles_root}/syntax/toml.vim


%files
%license LICENSE
%{vimfiles_root}/ftdetect/toml.vim
%{vimfiles_root}/ftplugin/toml.vim
%{vimfiles_root}/syntax/toml.vim


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20180615git85ba827
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20180615git85ba827
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20180615git85ba827
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Carl George <carl@george.computer> - 0-0.2.20180615git85ba827
- Latest upstream commit

* Thu Apr 05 2018 Carl George <carl@george.computer> - 0-0.1.20180306git624f024
- Include snapshot date in release

* Wed Apr 04 2018 Carl George <carl@george.computer> - 0-0.1.git624f024
- Initial package
