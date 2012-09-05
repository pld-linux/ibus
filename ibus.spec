# TODO
# - clean .py in %{_datadir}/{setup,ui/gtk} if possible
#
# Conditional build:
%bcond_without	gjsfile		# https://bugzilla.redhat.com/show_bug.cgi?id=657165
%bcond_without	static_libs	# don't build static library
#
%define		ibus_gjs_version	3.4.1.20120815
Summary:	Intelligent Input Bus for Linux OS
Summary(pl.UTF-8):	IBus - inteligentna szyna wejściowa dla Linuksa
Name:		ibus
Version:	1.4.2
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: http://code.google.com/p/ibus/downloads/list
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	4cc29edea599d465e1ee53c39da27a57
Source1:	%{name}.xinputd
Source100:	http://fujiwara.fedorapeople.org/ibus/gnome-shell/%{name}-gjs-%{ibus_gjs_version}.tar.gz
# Source100-md5:	8acf4ac4d1a7dfb9a0af9e755a8e7dba
Patch0:		%{name}-530711-preload-sys.patch
Patch1:		%{name}-541492-xkb.patch
Patch2:		%{name}-xx-bridge-hotkey.patch
Patch3:		%{name}-xx-setup-frequent-lang.patch
URL:		http://code.google.com/p/ibus/
BuildRequires:	GConf2-devel >= 2.12
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.10
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gobject-introspection-devel >= 0.6.8
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.35.0
BuildRequires:	iso-codes
BuildRequires:	libtool
BuildRequires:	python >= 1:2.5
BuildRequires:	python-dbus-devel >= 0.83.0
BuildRequires:	python-pygobject-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libxkbfile-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	GConf2 >= 2.12
Requires:	dbus >= 1.2.4
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	im-chooser
Requires:	iso-codes
Requires:	python-ibus = %{version}-%{release}
Requires:	python-pygtk-gtk
Requires:	python-pynotify
# input-keyboard-symbolic icon
Suggests:	gnome-icon-theme-symbolic
Requires(post,preun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
IBus means Intelligent Input Bus. It is an input framework for Linux
OS.

%description -l pl.UTF-8
IBus (Intelligent Input Bus) to inteligentna szyna wejściowa. Jest to
szkielet wprowadzania tekstu dla Linuksa.

%package libs
Summary:	IBus library
Summary(pl.UTF-8):	Biblioteka IBus
Group:		Libraries
Requires:	glib2 >= 1:2.26.0

%description libs
This package contains the IBus shared library.

%description libs -l pl.UTF-8
Ten pakiet zawiera bibliotekę współdzieloną IBus.

%package gtk2
Summary:	IBus im module for GTK+ 2.x
Summary(pl.UTF-8):	Moduł im IBus dla GTK+ 2.x
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	imsettings-gnome2
Requires(post):	glib2 >= 1:2.26.0

%description gtk2
This package contains IBus im module for GTK+ 2.x.

%description gtk2 -l pl.UTF-8
Ten pakiet zawiera moduł im IBus dla GTK+ 2.x.

%package gtk3
Summary:	IBus im module for GTK+ 3.x
Summary(pl.UTF-8):	Moduł im IBus dla GTK+ 3.x
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	imsettings-gnome3
Requires(post):	glib2 >= 1:2.26.0

%description gtk3
This package contains IBus im module for GTK+ 3.x.

%description gtk3 -l pl.UTF-8
Ten pakiet zawiera moduł im IBus dla GTK+ 3.x.

%package gnome3
Summary:	IBus gnome-shell-extension for GNOME3
Summary(pl.UTF-8):	Rozszerzenie gnome-shell IBus dla GNOME3
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-shell

%description gnome3
This is a transitional package which allows users to try out new IBus
GUI for GNOME3 in development. Note that this package will be marked
as obsolete once the integration has completed in the GNOME3 upstream.

%description gnome3 -l pl.UTF-8
Pakiet przejściowy pozwalający użytkownikom wypróbować nowe GUI IBus
dla GNOME3 w trakcie tworzenia. Uwaga: ten pakiet zostanie oznaczony
jako przestarzały po zakończeniu integracji w GNOME3.

%package devel
Summary:	Development files for IBus
Summary(pl.UTF-8):	Pliki programistyczne IBus
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel

%description devel
The ibus-devel package contains the header files for IBus.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe dla szkieletu IBus.

%package static
Summary:	Static ibus library
Summary(pl.UTF-8):	Biblioteka statyczna ibus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ibus library.

%description static -l pl.UTF-8
Biblioteka statyczna ibus.

%package apidocs
Summary:	Development documentation for IBus
Summary(pl.UTF-8):	Dokumentacja programisty dla szkieletu IBus
Group:		Development/Libraries
Requires:	gtk-doc-common
Conflicts:	ibus-devel < 1.4.2

%description apidocs
Development documentation for IBus.

%description apidocs -l pl.UTF-8
Dokumentacja programisty dla szkieletu IBus.

%package -n python-ibus
Summary:	Python interface to IBus framework
Summary(pl.UTF-8):	Pythonowy interfejs do szkieletu IBus
Group:		Development/Languages/Python
Requires:	python-dbus >= 0.83.0
Requires:	python-pygobject
Requires:	python-pygtk-pango
Requires:	python-pyxdg
Conflicts:	ibus < 1.4.2

%description -n python-ibus
Python interface to IBus framework.

%description -n python-ibus -l pl.UTF-8
Pythonowy interfejs do szkieletu IBus.

%package -n vala-ibus
Summary:	Vala API for ibus library
Summary(pl.UTF-8):	API języka Vala do biblioteki ibus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala

%description -n vala-ibus
Vala API for ibus library.

%description -n vala-ibus -l pl.UTF-8
API języka Vala do biblioteki ibus.

%prep
%setup -q
%if %{with gjsfile}
zcat %{SOURCE100} | tar xf -
%endif
cp -p client/gtk2/ibusimcontext.c client/gtk3/ibusimcontext.c
%patch0 -p1
%patch1 -p1
mv data/ibus.schemas.in data/ibus.schemas.in.in
%patch2 -p1
%patch3 -p1

%build
%if %{with gjsfile}
d=$(basename %{SOURCE100} .tar.gz)
cd $d
%configure
%{__make}
cd ..
%endif
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gtk-doc \
	--disable-silent-rules \
	--enable-bridge-hotkey \
	--enable-gconf \
	--enable-gtk2 \
	--enable-gtk3 \
	--enable-introspection \
	--enable-python \
	%{?with_static_libs:--enable-static} \
	--enable-surrounding-text \
	--enable-vala \
	--enable-xim \
	--enable-xkb \
	--with-html-dir=%{_gtkdocdir} \
	--with-no-snooper-apps='gnome-do,Do.*,firefox.*,.*chrome.*,.*chromium.*'

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{X11/xinit/xinput.d,xdg/autostart}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__sed} -e 's|@@LIB@@|%{_lib}|g' %{SOURCE1} >$RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d/ibus.conf

# correct location in upstream.
mv $RPM_BUILD_ROOT{%{_desktopdir},%{_sysconfdir}/xdg/autostart}/ibus.desktop

%if %{with gjsfile}
d=$(basename %{SOURCE100} .tar.gz)
%{__make} -C $d install \
	DESTDIR=$RPM_BUILD_ROOT
%{__rm} $RPM_BUILD_ROOT%{_localedir}/*/LC_MESSAGES/ibus-gjs.mo
%endif

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk*/*/immodules/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk*/*/immodules/*.a
%endif

%py_postclean

%find_lang %{name}10

# imsettings will start this daemon for us
%{__rm} $RPM_BUILD_ROOT/etc/xdg/autostart/ibus.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%gconf_schema_install ibus.schemas

%preun
%gconf_schema_uninstall ibus.schemas

%postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post gtk2
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%postun gtk2
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%post gtk3
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%postun gtk3
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%files -f %{name}10.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%config(noreplace) %verify(not md5 mtime size) /etc/X11/xinit/xinput.d/ibus.conf
%{_sysconfdir}/gconf/schemas/ibus.schemas
%attr(755,root,root) %{_bindir}/ibus-daemon
%attr(755,root,root) %{_bindir}/ibus-setup
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/ibus-gconf
%attr(755,root,root) %{_libexecdir}/ibus-ui-gtk
%attr(755,root,root) %{_libexecdir}/ibus-x11
%attr(755,root,root) %{_libexecdir}/ibus-engine-xkb
%attr(755,root,root) %{_libexecdir}/ibus-xkb
%{_datadir}/ibus
%{_desktopdir}/ibus-setup.desktop
%{_iconsdir}/hicolor/*/apps/ibus-*.png
%{_iconsdir}/hicolor/scalable/apps/ibus*.svg

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibus-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibus-1.0.so.0
%{_libdir}/girepository-1.0/IBus-1.0.typelib

%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/*/immodules/im-ibus.so

%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/*/immodules/im-ibus.so

%files gnome3
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/js/ui/status/ibus
%{_datadir}/gnome-shell/extensions/ibus-indicator@example.com

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibus-1.0.so
%{_pkgconfigdir}/ibus-1.0.pc
%{_includedir}/ibus-1.0
%{_datadir}/gir-1.0/IBus-1.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libibus-1.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/ibus

%files -n python-ibus
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/ibus
%{py_sitescriptdir}/ibus/*.py[co]
%dir %{py_sitescriptdir}/ibus/interface
%{py_sitescriptdir}/ibus/interface/*.py[co]

%files -n vala-ibus
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/ibus-1.0.vapi
%{_datadir}/vala/vapi/ibus-1.0.deps
