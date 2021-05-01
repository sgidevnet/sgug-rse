Name: xhtml2fo-style-xsl
Version: 20051222
Release: 20%{?dist}

Summary: Antenna House, Inc. XHTML to XSL:FO stylesheets
License: Copyright only
URL: http://www.antennahouse.com/XSLsample/XSLsample.htm

Requires: xhtml1-dtds
Requires: xml-common >= 0.6.3-8
Requires(post): libxml2
Requires(postun): libxml2

BuildArch: noarch
Source0: http://www.antennahouse.com/XSLsample/sample-xsl-xhtml2fo.zip
Source1: AntennaHouse-COPYRIGHT

%description
These XSL stylesheets allow you to transform any XHTML document to FO.
With a XSL:FO processor you could create PDF versions of XHTML documents.


%prep
%setup -c -q -n %{name}-%{version}
%__cp %{SOURCE1} .
%build


%install
%__rm -Rf $RPM_BUILD_ROOT
%__mkdir -p $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT%{_datadir}/sgml/xhtml1/xhtml2fo-stylesheets
%__mkdir -p $DESTDIR
%__cp *xsl $DESTDIR/

%files
%doc AntennaHouse-COPYRIGHT
%{_datadir}/sgml/xhtml1/xhtml2fo-stylesheets


%post
CATALOG=%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://www.antennahouse.com/XSLsample/sample-xsl-xhtml2fo/xhtml2fo.xsl" \
 "file://%{_datadir}/sgml/xhtml1/xhtml2fo-stylesheets/xhtml2fo.xsl" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://www.antennahouse.com/XSLsample/sample-xsl-xhtml2fo/xhtml2fo.xsl" \
 "file://%{_datadir}/sgml/xhtml1/xhtml2fo-stylesheets/xhtml2fo.xsl" $CATALOG

%postun
# remove entries only on removal of package
if [ "$1" = 0 ]; then
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
  "file://%{_datadir}/sgml/xhtml1/xhtml2fo-stylesheets/xhtml2fo.xsl" $CATALOG
fi


%changelog
* Sat Nov 28 2020 Daniel Hams <daniel.hams@gmail.com> - 20051222-20
- Fix the installation directories and post/postun requires

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20051222-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20051222-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20051222-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
