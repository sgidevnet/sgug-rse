%global commit  c6bc42404597c718e4a032a98e21e63321cbb05a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20190625

Name:           vim-pathogen
Version:        2.4
Release:        1.%{date}git%{shortcommit}%{?dist}
Summary:        Manage your runtimepath

License:        Vim
URL:            https://github.com/tpope/vim-pathogen
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        %{name}.metainfo.xml
BuildArch:      noarch

BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem

Requires:       vim-enhanced

%description
Manage your 'runtimepath' with ease. In practical terms, pathogen.vim makes it
super easy to install plugins and runtime files in their own private
directories.

For new users, I recommend using Vim's built-in package management instead:

  :help packages


%prep
%autosetup -n %{name}-%{commit} -p1


%install
mkdir -p        %{buildroot}%{vimfiles_root}
cp -r autoload  %{buildroot}%{vimfiles_root}
install -m 0644 -Dp %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license LICENSE
%doc README.markdown CONTRIBUTING.markdown
%{vimfiles_root}/autoload/*
%{_metainfodir}/*.xml


%changelog
* Sat May 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4-1.20190625gitc6bc424
- Update to latest git snapshot
- Add license file

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20181213gite9fb091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-2.20181213gite9fb091
- Initial package
