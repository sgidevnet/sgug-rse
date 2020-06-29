%global srcname subliminal

Name:           python-%{srcname}
Version:        2.1.0
Release:        2%{?dist}
Summary:        Python library to search and download subtitles
License:        MIT
URL:            https://github.com/Diaoul/subliminal
Source:         https://github.com/Diaoul/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Don't download sphinx interlink inventory files, instead use local ones (for those which are packaged)
Patch0:         python-subliminal_doc-inventories.patch
BuildArch:      noarch
BuildRequires:  python3-devel
# Doc building
BuildRequires:  python3-appdirs
BuildRequires:  python3-docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-babelfish
BuildRequires:  python3-guessit
BuildRequires:  python3-sphinxcontrib-programoutput
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-click
BuildRequires:  python-guessit-doc
BuildRequires:  python3-rarfile
BuildRequires:  python3-stevedore
BuildRequires:  python3-enzyme
BuildRequires:  python3-pysrt
BuildRequires:  python3-dogpile-cache
BuildRequires:  python3-rebulk
# Tests disabled
#BuildRequires:  python3-pytest-runner
#BuildRequires:  python3-pytz
#BuildRequires:  python3-rarfile
#BuildRequires:  python3-appdirs
#BuildRequires:  python3-six
#BuildRequires:  python3-pysrt
#BuildRequires:  python3-pbr
#BuildRequires:  python3-enzyme
#BuildRequires:  python3-stevedore
#BuildRequires:  python3-dogpile-cache
#BuildRequires:  python3-sympy
#BuildRequires:  python3-vcrpy
#BuildRequires:  python3-pytest-pep8
#BuildRequires:  python3-pytest-flakes
#BuildRequires:  python3-pytest-cov
#BuildRequires:  python3-guessit

%global _description\
Subliminal is a Python library to search and download subtitles.\
It comes with an easy to use yet powerful CLI suitable for direct use or\
cron jobs.\
\
Subliminal uses multiple providers to give users a vast choice and have\
a better chance to find the best matching subtitles. Current supported\
providers are:\
\
 - Addic7ed\
 - LegendasTV\
 - NapiProjekt\
 - OpenSubtitles\
 - Podnapisi\
 - Shooter\
 - TheSubDB\
 - TvSubtitles

%description %_description

%package -n python3-%{srcname}
Summary:        %summary
%{?python_provide:%python_provide python3-%{srcname}}
Suggests:       %{name}-doc

%description -n python3-%{srcname} %_description

%package doc
Summary:        %summary

%description doc %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

pushd docs
# Add folder containing subliminal script to PATH
export SPHINXBUILD=sphinx-build-3
PYTHONPATH=%{buildroot}%{python3_sitelib} PATH=$PATH:%{buildroot}%{_bindir} %make_build html
PYTHONPATH=%{buildroot}%{python3_sitelib} PATH=$PATH:%{buildroot}%{_bindir} %make_build text
PYTHONPATH=%{buildroot}%{python3_sitelib} PATH=$PATH:%{buildroot}%{_bindir} %make_build man
find . -name .buildinfo -type f -delete
popd
install -D -m 0644 docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1

%check
# Tests disabled because they connect to online services
#%%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%{_bindir}/subliminal
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info

%files doc
%doc README.rst docs/_build/html docs/_build/text
%license LICENSE
%{_mandir}/man1/%{srcname}.1*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.0-1
- Version 2.1.0

* Fri Jan 31 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.0.5-15
- BR: python3-rebulk
- Not needed to enable python dependency generator explicitly

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.5-9
- Enable python dependency generator

* Fri Dec 28 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-8
- Subpackage python2-subliminal has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-6
- Rebuilt for Python 3.7

* Sun Jun 10 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.5-5
- Add rarfile dependency

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 05 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.5-3
- Build docs

* Tue Aug 29 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.5-2
- Change Source URL
- Escape macros in comments
- Improve description

* Tue Aug 29 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.5-1
- Initial RPM release
