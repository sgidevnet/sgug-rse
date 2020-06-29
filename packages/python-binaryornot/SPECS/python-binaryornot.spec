%{?python_enable_dependency_generator}
%global modname binaryornot
%global sum A pure Python package to check if a file is binary or text


Name:               python-binaryornot
Version:            0.4.4
Release:            5%{?dist}
Summary:            %{sum}

License:            BSD
URL:                http://pypi.python.org/pypi/BinaryOrNot
Source0:            https://pypi.python.org/packages/source/b/binaryornot/binaryornot-%{version}.tar.gz
BuildArch:          noarch

%description
Ultra-lightweight pure Python package to guess whether a file is binary or
text, using a heuristic similar to Perl's pp_fttext and its analysis by
@eliben.

Has tests for these file types:
* Text: .txt, .css, .json, .svg, .js, .lua, .pl, .rst * Binary: .png, .gif,
.jpg, .tiff, .bmp, .DS_Store, .eot, .otf, .ttf, .woff, .rgb

Has tests for numerous encodings.


%package -n         python3-%{modname}
Summary:            %{sum}
BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-chardet >= 2.0.0
BuildRequires:      python3-hypothesis

%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-binaryornot
Ultra-lightweight pure Python package to guess whether a file is binary or
text, using a heuristic similar to Perl's pp_fttext and its analysis by
@eliben.

Has tests for these file types:
* Text: .txt, .css, .json, .svg, .js, .lua, .pl, .rst * Binary: .png, .gif,
.jpg, .tiff, .bmp, .DS_Store, .eot, .otf, .ttf, .woff, .rgb

Has tests for numerous encodings.


%package -n         python-%{modname}-docs
Summary:            Documentation for python-binaryornot
BuildRequires:      python3-sphinx

%description -n python-%{modname}-docs
Documentation for python-binaryornot


%prep
%autosetup -n %{modname}-%{version}

# sed equivalent to
# https://github.com/audreyr/binaryornot/commit/38dee57986c6679d99
# not present in 0.4.4
sed -i -e 's|average_size=|max_size=|' tests/test_check.py

rm -rf %{modname}.egg-info


%build
%py3_build

make -C docs html PYTHONPATH=$(pwd)


%install
%py3_install

%check
%{__python3} setup.py test

rm -rf docs/_build/html/.buildinfo


%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*

%files -n python-%{modname}-docs
%doc docs/_build/html


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.4-1
- Update to 0.4.4

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Charalampos Stratakis <cstratak@redhat.com> - 0.4.3-6
- Fix compatibility with hypothesis 4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.3-4
- Enable python dependency generator

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-3
- Subpackage python2-binaryornot has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.3-1
- Update to 0.4.3

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-9
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.0-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Nov 30 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.0-2
- Update the spec to the latest guidelines, generating two sub-packages one for
  py2 and one for py3
- Build the doc and place it in a -docs sub-package

* Fri Nov 27 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.0-1
- initial package for Fedora
