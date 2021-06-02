%global commit  6b7cdecff252474fe560d32c6f05641f3c5952c7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20191209

Name:           vim-trailing-whitespace
Version:        1.0
Release:        1.%{date}git%{shortcommit}%{?dist}
Summary:        Highlights trailing whitespace in red and provides :FixWhitespace to fix it

License:        CC-BY-SA
URL:            https://github.com/bronson/vim-trailing-whitespace
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        %{name}.metainfo.xml
BuildArch:      noarch

BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem

Requires:       vim-enhanced

%description
This plugin causes all trailing whitespace to be highlighted in red.

To fix the whitespace errors, just call :FixWhitespace. By default it operates
on the entire file. Pass a range (or use V to select some lines) to restrict
the portion of the file that gets fixed.


%prep
%autosetup -n %{name}-%{commit} -p1


%install
mkdir -p        %{buildroot}%{vimfiles_root}
cp -ar plugin   %{buildroot}%{vimfiles_root}
install -m0644 -Dp %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%doc README doc/*
%{vimfiles_root}/plugin/*
%{_metainfodir}/*.xml


%changelog
* Fri Jun 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0-1.20191209git6b7cdec
- Update to latest git snapshot

* Thu Oct 03 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0-1.20170923git4c59654
- Initial package
