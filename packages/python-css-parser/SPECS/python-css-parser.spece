Name:           python-css-parser
Version:        1.0.4
Release:        8%{?dist}
Summary:        Parse and build Cascading Style Sheets

%global forgeurl https://github.com/ebook-utils/css-parser
%global commit 1bd50d05d832ede559c1ae96c714bb124f0b790b
%forgemeta

License:        LGPLv3
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel
# for tests
BuildRequires:  python3-chardet

%global _description %{expand:
A fork of the cssutils project based on version 1.0.2. This fork includes
general bug fixes and extensions specific to editing and working with ebooks.}

%description %_description

%package -n python3-css-parser
Summary:        %{summary}
%{?python_provide:%python_provide python3-css-parser}

%description -n python3-css-parser %_description

%prep
%forgesetup

%build
sed -r -i '1{/.usr.bin.env python/d;}' src/css_parser/*py src/css_parser/*/*py

%py3_build

%install
%py3_install

%check
%{__python3} run_tests.py

%files -n python3-css-parser
%{python3_sitelib}/css_parser/
%{python3_sitelib}/css_parser-%{version}-py%{python3_version}.egg-info/
%doc README.md
%license COPYING COPYING.LESSER

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-8
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.4-7
- Switch to version of patches merged by upstream (#1792929)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.4-4
- Subpackage python2-css-parser has been removed (#1741018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.4-1
- Initial packaging
