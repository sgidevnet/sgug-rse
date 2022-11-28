Name:           vim-airline
Version:        0.11
Release:        1%{?dist}
Summary:        Lean & mean status/tabline for vim that's light as air

License:        MIT
URL:            https://github.com/vim-airline/vim-airline
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.metainfo.xml
BuildArch:      noarch

BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem
Requires:       vim-enhanced

%description
%{summary}.

When the plugin is correctly loaded, Vim will draw a nice statusline at the
bottom of each window.


%prep
%autosetup -p1


%install
mkdir -p                        %{buildroot}%{vimfiles_root}
cp -r {autoload,plugin}         %{buildroot}%{vimfiles_root}
install -m 0644 -Dp %{SOURCE1}  %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license LICENSE
%doc README.md CHANGELOG.md CONTRIBUTING.md doc/*
%{vimfiles_root}/autoload/*
%{vimfiles_root}/plugin/*
%{_metainfodir}/*.xml


%changelog
* Sun Nov 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.11-1
- Update to 0.11

* Sun Oct 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10-5.20191011git297ca3d
- Update to latest git snapshot

* Tue Oct 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10-2.20190911git89d1d43
- Initial package
