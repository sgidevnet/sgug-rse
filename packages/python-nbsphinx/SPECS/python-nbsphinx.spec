# Created by pyp2rpm-3.2.2
%global pypi_name nbsphinx

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        1%{?dist}
Summary:        Jupyter Notebook Tools for Sphinx

License:        MIT
URL:            http://nbsphinx.rtfd.io/
Source0:        %{pypi_source}
Patch1:         0001-Allow-errors-and-add-a-note-in-one-doc-notebook.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-ipykernel
BuildRequires:  python3-ipython-sphinx
BuildRequires:  python3-jupyter-client
BuildRequires:  python3-nbconvert
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-bibtex
BuildRequires:  python3-sphinx-copybutton
BuildRequires:  python3-sphinxcontrib-rsvgconverter
BuildRequires:  python3-sphinx-gallery
BuildRequires:  python3-sphinx-last-updated-by-git
BuildRequires:  git
BuildRequires:  pandoc

%description
nbsphinx is a Sphinx extension that provides a source parser for *.ipynb
files. Custom Sphinx directives are used to show Jupyter Notebook code cells
(and of course their results) in both HTML and LaTeX output. Unevaluated
notebooks, i.e. notebooks without stored output cells, will be automatically
executed during the Sphinx build process.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
nbsphinx is a Sphinx extension that provides a source parser for *.ipynb
files. Custom Sphinx directives are used to show Jupyter Notebook code cells
(and of course their results) in both HTML and LaTeX output. Unevaluated
notebooks, i.e. notebooks without stored output cells, will be automatically
executed during the Sphinx build process.

%package -n python-%{pypi_name}-doc
Summary:        nbsphinx documentation
%description -n python-%{pypi_name}-doc
Documentation for nbsphinx

%prep
%autosetup -n %{pypi_name}-%{version} -S git

%build
%py3_build
# fake the git tag for docs to put the right version in
git tag %{version}
# generate html docs 
PYTHONPATH=build/lib sphinx-build-3 doc html
# remove the sphinx-build leftovers
rm -rf html/{.doctrees,.buildinfo,conf.py}

%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst

%{python3_sitelib}/__pycache__/%{pypi_name}*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html 

%changelog
* Thu Jun 04 2020 Charalampos Stratakis <cstratak@redhat.com> - 0.7.0-1
- Update to 0.7.0 (#1757082)

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-2
- Explicitly require nbconvert

* Wed Feb 27 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-1
- Update to 0.4.2 (#1680237)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.17-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Lumír Balhar <lbalhar@redhat.com> - 0.2.17-1
- New upstream version
- Fix FTBFS

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Miro Hrončok <mhroncok@redhat.com> - 0.2.13-1
- Initial package
