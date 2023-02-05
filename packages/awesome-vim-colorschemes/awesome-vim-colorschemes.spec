%global commit 41a0d9ea4dac077c2050ceaf144f9ed72d6849d8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20200911

Name: awesome-vim-colorschemes
Version: 0
Release: 11.%{date}git%{shortcommit}%{?dist}
Summary: Collection of color schemes for Neo/vim, merged for quick use
BuildArch: noarch

# You can find the individual license in the actual vim file, or find the
# appropriate README in docs/
# * https://github.com/rafi/awesome-vim-colorschemes/issues/12
License: Vim and MIT and CC-BY

URL: https://github.com/rafi/awesome-vim-colorschemes
Source0: %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1: %{name}.metainfo.xml

# Remove executable bit & Fix wrong file end of line encoding
# * https://github.com/rafi/awesome-vim-colorschemes/pull/13
Patch0: https://github.com/rafi/awesome-vim-colorschemes/pull/13#/remove-executable-bit-&-fix-wrong-file-end-of-line-encoding.patch

BuildRequires: libappstream-glib
BuildRequires: vim-filesystem

Requires: vim-enhanced

%description
Collection of awesome color schemes for Neo/vim, merged for quick use.


%prep
%autosetup -n %{name}-%{commit} -p1


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -a {autoload,colors} %{buildroot}%{vimfiles_root}
install -Dpm0644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml


%files
%doc README.md docs/
%{vimfiles_root}/autoload/*
%{vimfiles_root}/colors/*
%{_metainfodir}/*.xml


%changelog
* Tue Oct 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-11.20200911git41a0d9e
- build(update): commit 41a0d9e

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20191209gitb5037cb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20191209gitb5037cb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-8.20191209gitb5037cb
- Remove executable bit & Fix wrong file end of line encoding

* Fri Jan 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-7.20191209gitb5037cb
- Preserve timestamps during copy

* Mon Dec 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-6.20191209gitb5037cb
- Update to latest git snapshot
- Add missed license in spec file

* Sun Sep 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-6.20190921git21f5c63
- Initial package
